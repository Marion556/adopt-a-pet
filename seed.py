from models import db, Pet
from app import app

db.drop_all()
db.create_all()

DEFAULT_PET_PHOTO = 'https://unsplash.com/photos/dQ5G0h7sLno'

ONeil = Pet(name='ONeil', species='cat', photo_url='https://unsplash.com/photos/BsrOgzeI6QA',
            age=14, notes='old sweet boy', available=True)
Merlin = Pet(name='Merlin', species='dog', photo_url='https://unsplash.com/photos/Od4VSPaG1-4',
            age=3, notes='Likes belly scratches', available=True)
Bathtub = Pet(name='Bathtub', species='cat', photo_url='https://unsplash.com/photos/NfQFX439fDM',
             age=2, notes='young and cute', available=True)
Bidule = Pet(name='Bidule', species='guinea pig', photo_url='https://unsplash.com/photos/mwwRDU_ekjw',
             age=3, notes='Very affectionate', available=True)

db.session.add_all([Oneil, Merlin, Bathtub, Bidule])

db.session.commit()