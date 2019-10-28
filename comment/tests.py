from django.test import TestCase

# Create your tests here.

import uuid

Uid = uuid.uuid4().hex
print(Uid)
print(len(Uid))
