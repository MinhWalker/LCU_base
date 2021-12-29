from models.partner import Partner
from base import session, engine, Base

# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = session()

# 4 - create Partner
bourne_identity = Partner(id=1, name="The Bourne Identity", description="testing")
furious_7 = Partner(id=2, name="Furious 7", description="testing")
pain_and_gain = Partner(id=3, name="Pain & Gain", description="testing")


# 6 - persists data
session.add(bourne_identity)
session.add(furious_7)
session.add(pain_and_gain)


# 10 - commit and close session
session.commit()
session.close()