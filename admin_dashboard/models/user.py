class User():
    id: str
    email: str
    name: str
    password_hash: str
    is_admin: bool


    def __init__(self, id, email, name, password_hash, is_admin) -> None:
        self.id = id
        self.email = email
        self.name = name
        self.password_hash = password_hash
        self.is_admin = is_admin
    
    @staticmethod
    def get_by_id(id: str) -> 'User':
        # make query to get user from database
        return User(None, None, None, None, True)
