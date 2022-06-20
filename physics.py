DEFAULT_G = 2500
g = DEFAULT_G

DEFAULT_FRICTION = 1000
FRICTION = DEFAULT_FRICTION

class Physics:
    def get_friction():
        return FRICTION

    def set_friction(new):
        global FRICTION
        FRICTION = new

    def get_gravity():
        return g

    def set_gravity(new):
        global g
        g = new