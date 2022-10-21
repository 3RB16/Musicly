from django.test import TestCase,RequestFactory


from .models import RoomModel
from .views import RoomView
from.serializers import RoomSerializer
from .utils import generate_unique_code

class RoomTests(TestCase):
    def setUp(self):
        RoomModel.objects.create(code = generate_unique_code , host = 'muhammad arbi',
            guest_can_pause = False , votes_to_skip = 1
        )    
    def test_get_all(self):
        request = RequestFactory().get('/api/room')
        response = RoomView.as_view()(request)
        all_rooms = RoomSerializer(RoomModel.objects.all() , many = True)
        self.assertEqual(all_rooms.data,response.data)