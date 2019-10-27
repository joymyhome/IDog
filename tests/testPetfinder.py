import unittest

import sys
sys.path.append('../')

import petfinder
from Dog import Dog

class TestPetFinder(unittest.TestCase):
    def setUp(self):
        # Input with all information
        self.input = {'id': 45000754, 'organization_id': 'CA1331', 'url': 'https://www.petfinder.com/dog/cooper-45000754/ca/sacramento/chows-plus-ca1331/?referrer_id=e86acdb9-2e4b-4d8c-b9e1-11bd004d5517', 'type': 'Dog', 'species': 'Dog', 'breeds': {'primary': 'Golden Retriever', 'secondary': 'Husky', 'mixed': True, 'unknown': False}, 'colors': {'primary': 'Golden', 'secondary': None, 'tertiary': None}, 'age': 'Young', 'gender': 'Male', 'size': 'Large', 'coat': 'Medium', 'attributes': {'spayed_neutered': True, 'house_trained': True, 'declawed': None, 'special_needs': False, 'shots_current': True}, 'environment': {'children': None, 'dogs': None, 'cats': None}, 'tags': [], 'name': 'Cooper!', 'description': 'This handsome guy is Cooper!  He is around 1.5 - 2 years old. What a friendly, loving sweet dog. He...', 'photos': [{'small': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/45000754/4/?bust=1561690767&width=100', 'medium': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/45000754/4/?bust=1561690767&width=300', 'large': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/45000754/4/?bust=1561690767&width=600', 'full': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/45000754/4/?bust=1561690767'}, {'small': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/45000754/1/?bust=1560732647&width=100', 'medium': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/45000754/1/?bust=1560732647&width=300', 'large': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/45000754/1/?bust=1560732647&width=600', 'full': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/45000754/1/?bust=1560732647'}, {'small': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/45000754/2/?bust=1560732725&width=100', 'medium': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/45000754/2/?bust=1560732725&width=300', 'large': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/45000754/2/?bust=1560732725&width=600', 'full': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/45000754/2/?bust=1560732725'}, {'small': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/45000754/5/?bust=1560732874&width=100', 'medium': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/45000754/5/?bust=1560732874&width=300', 'large': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/45000754/5/?bust=1560732874&width=600', 'full': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/45000754/5/?bust=1560732874'}, {'small': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/45000754/3/?bust=1561690767&width=100', 'medium': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/45000754/3/?bust=1561690767&width=300', 'large': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/45000754/3/?bust=1561690767&width=600', 'full': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/45000754/3/?bust=1561690767'}], 'status': 'adoptable', 'published_at': '2019-06-17T01:04:35+0000', 'contact': {'email': 'crazy4chows@sbcglobal.net', 'phone': None, 'address': {'address1': None, 'address2': None, 'city': 'Sacramento', 'state': 'CA', 'postcode': '95842', 'country': 'US'}}, '_links': {'self': {'href': '/v2/animals/45000754'}, 'type': {'href': '/v2/types/dog'}, 'organization': {'href': '/v2/organizations/ca1331'}}}
        # Input without picture of a dog
        self.input2 = {'id': 45000754, 'organization_id': 'CA1331', 'url': 'https://www.petfinder.com/dog/cooper-45000754/ca/sacramento/chows-plus-ca1331/?referrer_id=e86acdb9-2e4b-4d8c-b9e1-11bd004d5517', 'type': 'Dog', 'species': 'Dog', 'breeds': {'primary': 'Golden Retriever', 'secondary': 'Husky', 'mixed': True, 'unknown': False}, 'colors': {'primary': 'Golden', 'secondary': None, 'tertiary': None}, 'age': 'Young', 'gender': 'Male', 'size': 'Large', 'coat': 'Medium', 'attributes': {'spayed_neutered': True, 'house_trained': True, 'declawed': None, 'special_needs': False, 'shots_current': True}, 'environment': {'children': None, 'dogs': None, 'cats': None}, 'tags': [], 'name': 'Cooper!', 'description': 'This handsome guy is Cooper!  He is around 1.5 - 2 years old. What a friendly, loving sweet dog. He...', 'photos': [], 'status': 'adoptable', 'published_at': '2019-06-17T01:04:35+0000', 'contact': {'email': 'crazy4chows@sbcglobal.net', 'phone': None, 'address': {'address1': None, 'address2': None, 'city': 'Sacramento', 'state': 'CA', 'postcode': '95842', 'country': 'US'}}, '_links': {'self': {'href': '/v2/animals/45000754'}, 'type': {'href': '/v2/types/dog'}, 'organization': {'href': '/v2/organizations/ca1331'}}}

    # Returns true if _convert_to_dog function creates the same object of Dog
    # Test when all information is provided
    def test_convert_to_dog(self):
        self.assertEqual(petfinder._convert_to_dog(self.input), Dog(45000754, 'CA1331', 'Golden Retriever', 'Husky', 'Young', 'Male', True, 'Cooper!', 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/45000754/4/?bust=1561690767&width=600', 'crazy4chows@sbcglobal.net', None,'Sacramento', [], {'children': None, 'dogs': None, 'cats': None}, 'This handsome guy is Cooper!  He is around 1.5 - 2 years old. What a friendly, loving sweet dog. He...', 'Sacramento CA 95842'))

    # Returns true if _convert_to_dog function creates the same object of Dog
    # Test if no picture provided
    def test_convert_to_dog2(self):
        self.assertEqual(petfinder._convert_to_dog(self.input2), Dog(45000754, 'CA1331', 'Golden Retriever', 'Husky', 'Young', 'Male', True, 'Cooper!', None, 'crazy4chows@sbcglobal.net', None,'Sacramento', [], {'children': None, 'dogs': None, 'cats': None}, 'This handsome guy is Cooper!  He is around 1.5 - 2 years old. What a friendly, loving sweet dog. He...', 'Sacramento CA 95842'))

if __name__ == '__main__':
    unittest.main()
