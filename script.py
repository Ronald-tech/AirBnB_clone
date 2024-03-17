from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

s = State(name='Nairobi')
s.save()

c = City(name='Nairobi', state_id=s.id)
c.save()

u = User(email='lynnetteagneta@gmail.com', password='lU8jbsldsk')
u.save()

a = Amenity(name='Wifi')
a.save()

p = Place(city_id=c.id, user_id=u.id, name='Cottage',
          number_rooms=2, number_bathrooms=2, price_by_night=10, max_guest=3)
p.description = "Lorem ipsum dolor sit amet, officia excepteur ex fugiat reprehenderit enim labore culpa sint ad nisi Lorem pariatur mollit ex esse exercitation amet. Nisi anim cupidatat excepteur officia. Reprehenderit nostrud nostrud ipsum Lorem est aliquip amet voluptate voluptate dolor minim nulla est proident. Nostrud officia pariatur ut officia. Sit irure elit esse ea nulla sunt ex occaecat reprehenderit commodo officia dolor Lorem duis laboris cupidatat officia voluptate. Culpa proident adipisicing id nulla nisi laboris ex in Lorem sunt duis officia eiusmod. Aliqua reprehenderit commodo ex non excepteur duis sunt velit enim. Voluptate laboris sint cupidatat ullamco ut ea consectetur et est culpa et culpa duis."
p.amenities = [a]
p.save()


r = Review(place_id=p.id, user_id=u.id, text='Kisumu is the best')
