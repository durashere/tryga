class Npc:
    def __init__(self, name, job):
        self.name = name
        self.job = job
        # self.zone = 'BEACH_FISHERMANS_HUT'


NPCS = {}
NPCS['FISHERMAN'] = Npc('Fisherman', 'Fisherman')
