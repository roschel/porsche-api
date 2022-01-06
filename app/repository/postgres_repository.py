from sqlmodel import select, Session


class PostgresRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self, model):
        with self.session as session:
            results = session.exec(select(model)).all()
            return results

    def save(self, model):
        with self.session as session:
            session.add(model)
            session.commit()
            session.refresh(model)

        return model
