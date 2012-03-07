from sc2match.models import PlayerResult, Map #Match
from profiles.models import Player

def as_signal(sender, instance, created, raw, **kwargs):
    if created:
        parse_replay(instance)

def parse_replay(match):

    match.players.all().delete()
    match.map, created = Map.objects.get_or_create(
        name=match.replay.map
    )


    for p in match.replay.players:
        player, created = Player.objects.get_or_create(
            username=p.name,
            battle_net_url=p.url
        )
        result = None
        if p.result == 'Win':
            result = True
        elif p.result == 'Loss':
            result = False

        if p.pick_race == 'Random':
            random=True
        else:
            random=False

        PlayerResult.objects.create(
            match=match,
            player=player,
            result=result,
            random=random,
            color='rgb(%(r)s, %(g)s, %(b)s)' % p.color
        )

    match.save()

