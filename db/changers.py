from db import Base


def add_object(object: Base) -> None:
    Base.db_session.add(object)
    Base.db_session.commit()


def delete_object(object: Base) -> None:
    Base.db_session.delete(object)
    Base.db_session.commit()
