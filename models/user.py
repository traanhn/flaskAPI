from data.database import database


class UserModel(database.Model):
    __tablename__ = 'users'

    user_id = database.Column(database.Integer, primary_key=True)
    first_name = database.Column(database.String)
    last_name = database.Column(database.String)
    gender = database.Column(database.String)
    email = database.Column(database.String)
    ip_address = database.Column(database.String)
    country_code = database.Column(database.String)

    def __init__(self, first_name, last_name, gender, email, ip_address, country_code):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.ip_address = ip_address
        self.country_code = country_code

    def json(self):
        return {
                'user_id': self.user_id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'gender': self.gender,
                'email': self.email,
                'ip_address': self.ip_address,
                'country_code': self.country_code
                }

    def save_to_db(self):
        database.session.add(self)
        database.session.commit()

    def delete_from_db(self):
        database.session.delete(self)
        database.session.commit()

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()


