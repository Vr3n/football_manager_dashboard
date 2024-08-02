from django.db import models

# Create your models here.


class PlayerAttribs(models.Model):
    det = models.PositiveIntegerField(default=0)
    mins = models.PositiveIntegerField(default=0)
    apps = models.PositiveIntegerField(default=0)
    substitute_apps = models.PositiveIntegerField(default=0)
    wor = models.PositiveIntegerField(default=0)
    sta = models.PositiveIntegerField(default=0)
    tea = models.PositiveIntegerField(default=0)
    cnt = models.PositiveIntegerField(default=0)
    acc = models.PositiveIntegerField(default=0)
    vis = models.PositiveIntegerField(default=0)
    thr = models.PositiveIntegerField(default=0)
    tec = models.PositiveIntegerField(default=0)
    tck = models.PositiveIntegerField(default=0)
    tro = models.PositiveIntegerField(default=0)
    ref = models.PositiveIntegerField(default=0)
    pen = models.PositiveIntegerField(default=0)
    pas = models.PositiveIntegerField(default=0)
    pac = models.PositiveIntegerField(default=0)
    one_v_one = models.PositiveIntegerField(default=0)
    otb = models.PositiveIntegerField(default=0)
    mar = models.PositiveIntegerField(default=0)
    lth = models.PositiveIntegerField(default=0)
    lon = models.PositiveIntegerField(default=0)
    ldr = models.PositiveIntegerField(default=0)
    kic = models.PositiveIntegerField(default=0)
    jum = models.PositiveIntegerField(default=0)
    hea = models.PositiveIntegerField(default=0)
    han = models.PositiveIntegerField(default=0)
    fre = models.PositiveIntegerField(default=0)
    fla = models.PositiveIntegerField(default=0)
    flr = models.PositiveIntegerField(default=0)
    fin = models.PositiveIntegerField(default=0)
    ecc = models.PositiveIntegerField(default=0)
    dri = models.PositiveIntegerField(default=0)
    cro = models.PositiveIntegerField(default=0)
    cor = models.PositiveIntegerField(default=0)
    cmp = models.PositiveIntegerField(default=0)
    cmd = models.PositiveIntegerField(default=0)
    bra = models.PositiveIntegerField(default=0)
    bal = models.PositiveIntegerField(default=0)
    ant = models.PositiveIntegerField(default=0)
    agg = models.PositiveIntegerField(default=0)
    agi = models.PositiveIntegerField(default=0)
    aer = models.PositiveIntegerField(default=0)
    dec = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class PlayerStats(models.Model):
    hdrs_a = models.PositiveIntegerField(default=0)
    tck_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True)
    tck_w = models.PositiveIntegerField(default=0)
    tck_r = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    tck_a = models.PositiveIntegerField(default=0)
    shot_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    short_percent = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    sht_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    sht = models.PositiveIntegerField(default=0)
    shots = models.PositiveIntegerField(default=0)
    svt = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    svp = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    svh = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    sv_percentage = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    pr_passes_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    pr_passes = models.PositiveIntegerField(default=0)
    pres_c = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    pres_a_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    pres_a = models.PositiveIntegerField(default=0)
    poss_won_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    poss_lost_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    ps_c_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    ps_c = models.BigIntegerField(default=0)
    pas_percentage = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    ps_a_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    pas_a = models.PositiveIntegerField(default=0)
    op_kp_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    op_kp = models.PositiveIntegerField(default=0)
    off = models.PositiveIntegerField(default=0)
    gl_mst = models.PositiveIntegerField(default=0)
    k_tck_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    k_tck = models.PositiveIntegerField(default=0)
    k_ps_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    k_pas = models.PositiveIntegerField(default=0)
    k_hdrs_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    int_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    itc = models.PositiveIntegerField(default=0)
    sprints_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    hdr_percentage = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    hdrs_w_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    hdrs = models.PositiveIntegerField(default=0)
    xsv_percentage = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    xg_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    xgp = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    xg_shot_percentage = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    drb_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    drb = models.PositiveIntegerField(default=0)
    distance = models.PositiveIntegerField(default=0)
    cr_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    cr_c = models.PositiveIntegerField(default=0)
    crs_a_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    crs_c_a = models.PositiveIntegerField(default=0)
    conv_percentage = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    ccc = models.PositiveIntegerField(default=0)
    chc_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    blk_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    blk = models.PositiveIntegerField(default=0)
    asts_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    at_apps = models.PositiveIntegerField(default=0)
    xg = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    saves_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    tgls_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    tcon_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    starts = models.PositiveIntegerField(default=0)
    red = models.PositiveIntegerField(default=0)
    pts_per_game = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    pom = models.PositiveIntegerField(default=0)
    pen_r = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    pens_s = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    pens_saved_ratio = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    pens_faced = models.PositiveIntegerField(default=0)
    pens = models.PositiveIntegerField(default=0)
    np_xg_per_90 = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    np_xg = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    last_gl = models.PositiveIntegerField(default=0)
    last_c = models.PositiveIntegerField(default=0)
    mins_per_game = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    lmr = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    last_5_games = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    last_5_ft_games = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    int_av_rat = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    int_conc = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    int_ast = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    int_apps = models.PositiveIntegerField(default=0)
    gls_per_90 = models.PositiveIntegerField(default=0)
    conc = models.PositiveIntegerField(default=0)
    gls = models.PositiveIntegerField(default=0)
    won = models.PositiveIntegerField(default=0)
    g_mis = models.PositiveIntegerField(default=0)
    lost = models.PositiveIntegerField(default=0)
    draw = models.PositiveIntegerField(default=0)
    g_win_percentage = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    fls = models.PositiveIntegerField(default=0)
    fa = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class Team(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tactic(models.Model):
    name = models.CharField(max_length=250)


class SquadPlayer(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=250)
    uid = models.PositiveIntegerField(default=0)
    age = models.CharField(max_length=3, null=True, blank=True)
    position = models.CharField(max_length=250, null=True, blank=True)
    wage = models.DecimalField(
        max_digits=19, decimal_places=4, null=True, blank=True)
    nationality = models.CharField(max_length=250, null=True, blank=True)
    personality = models.CharField(max_length=250, null=True, blank=True)
    agreed_playing_time = models.CharField(
        max_length=250, null=True, blank=True)
    playing_time_happiness = models.CharField(
        max_length=250, null=True, blank=True)
    preferred_foot = models.CharField(
        max_length=250, null=True, blank=True)
    height = models.PositiveIntegerField(default=0)
    pros = models.CharField(
        max_length=250, null=True, blank=True)
    cons = models.CharField(
        max_length=250, null=True, blank=True)

    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)


class SquadPlayerAttributes(PlayerAttribs):
    squad_player = models.ForeignKey(SquadPlayer, on_delete=models.CASCADE)


class SquadPlayerStats(PlayerStats):
    squad_player = models.ForeignKey(SquadPlayer, on_delete=models.CASCADE)
