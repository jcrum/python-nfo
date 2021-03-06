
"""
class OODictElementMixin:

	override_with_type = False

	def set(self, value):
		raise NotImplementedError()
"""

class Mixin:
	"""Mixin that presents the items in `data` as instance attributes of the subclass."""

	data = {}

	def update_data(self, new_data):
		for key, value in new_data.items():
			if key in self.data:
				self.set_data(key, value)

	def get_data(self, key):
		"""Return the object at dictionary key `key`."""
		return self.data[key]

	def set_data(self, key, value):
		"""Sets the value of the object at key `key`.

		Set the value of the object at dictionary key `key` by calling it with
		the argument `value`.

		This lets the object handle the setting of the value in a more complex
		way.
		"""
		if  (self.data[key].override_with_type is not False and
				isinstance(value, self.data[key].override_with_type)):
			self.data[key] = value
		else:
			self.data[key].set(value)

	def __setattr__(self, attr, value):
		if attr in self.data:
			self.set_data(attr, value)
		else:
			return super().__setattr__(attr, value)

	def __getattr__(self, attr):
		if attr in self.data:
			return self.get_data(attr)
		else:
			if hasattr(super(), '__getattr__'):
				return super().__getattr__(attr)  # pylint: disable=no-member
		raise AttributeError(attr)
