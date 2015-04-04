import time as s_time
import csv

# '2014-11-18 0': 1416240000.0, '2014-11-19 0': 1416326400.0, '2014-11-20 0': 1416412800.0, '2014-11-21 0': 1416499200.0, '2014-11-22 0': 1416585600.0, '2014-11-23 0': 1416672000.0, '2014-11-24 0': 1416758400.0, '2014-11-25 0': 1416844800.0, '2014-11-26 0': 1416931200.0, '2014-11-27 0': 1417017600.0, '2014-11-28 0': 1417104000.0, '2014-11-29 0': 1417190400.0, '2014-11-30 0': 1417276800.0, '2014-12-01 0': 1417363200.0, '2014-12-02 0': 1417449600.0, '2014-12-03 0': 1417536000.0, '2014-12-04 0': 1417622400.0, '2014-12-05 0': 1417708800.0, '2014-12-06 0': 1417795200.0, '2014-12-07 0': 1417881600.0, '2014-12-08 0': 1417968000.0, '2014-12-09 0': 1418054400.0, '2014-12-10 0': 1418140800.0, '2014-12-11 0': 1418227200.0, '2014-12-12 0': 1418313600.0, '2014-12-13 0': 1418400000.0, '2014-12-14 0': 1418486400.0, '2014-12-15 0': 1418572800.0, '2014-12-16 0': 1418659200.0, '2014-12-17 0': 1418745600.0, '2014-12-18 0': 1418832000.0, '2014-12-19 0': 1418918400.0,

fp = open("tianchi_mobile_recommend_train_user.csv", 'r')
wf = open("feat1.csv", 'wb')
wp = csv.writer(wf)

ui_cart = {}
fp.readline()
count = 0
for line in fp:
    count += 1
    if count % 10000 == 0:
        print count
    (ui, ii, bt, ug, ca, ti) = line.split(',')
    # init feature set.
    if (ui, ii) not in ui_cart:
        ui_cart[(ui, ii)] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i_time = s_time.mktime(s_time.strptime(ti.strip(), '%Y-%m-%d %H'))
    # bought on the 18th, used as label
    if bt == '4' and 1418832000 < i_time < 1418918400:
        ui_cart[(ui, ii)][0] += 1
    if i_time < 1418832000:
        # added to cart within 10 days
        if bt == '3' and 1417968000 < i_time:
            ui_cart[(ui, ii)][1] += 1
        # added to cart within 5 days
        if bt == '3' and 1418400000 < i_time:
            ui_cart[(ui, ii)][2] += 1
        # added to cart within 2 days
        if bt == '3' and 1418659200 < i_time:
            ui_cart[(ui, ii)][3] += 1
        # collected within 10 days
        if bt == '2' and 1417968000 < i_time:
            ui_cart[(ui, ii)][4] += 1
        # collected within 5 days
        if bt == '2' and 1418400000 < i_time:
            ui_cart[(ui, ii)][5] += 1
        # collected within 2 days
        if bt == '2' and 1418659200 < i_time:
            ui_cart[(ui, ii)][6] += 1
        # viewed within 10 days
        if bt == '1' and 1417968000 < i_time:
            ui_cart[(ui, ii)][7] += 1
        # viewed within 5 days
        if bt == '1' and 1418400000 < i_time:
            ui_cart[(ui, ii)][8] += 1
        # viewed within 2 days
        if bt == '1' and 1418659200 < i_time:
            ui_cart[(ui, ii)][9] += 1
        # bought within 10 days
        if bt == '4' and 1417968000 < i_time:
            ui_cart[(ui, ii)][10] += 1
        # bought within 5 days
        if bt == '4' and 1418400000 < i_time:
            ui_cart[(ui, ii)][11] += 1
        # bought within 2 days
        if bt == '4' and 1418659200 < i_time:
            ui_cart[(ui, ii)][12] += 1

for (k, v) in ui_cart.iteritems():
    wp.writerow((k[0], k[1]) + tuple(v))

wf.close()