def areYouPlayingBanjo(name):
    return "{} plays banjo".format(name) if name[0].upper()=='R' or name[0]=='r' else "{} does not play banjo"