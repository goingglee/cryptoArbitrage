#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 21:45:17 2017

@author: garrettlee
"""

import requests

pairs = ['BTC_BCN', 'BTC_BELA', 'BTC_BLK', 'BTC_BTCD', 'BTC_BTM', 'BTC_BTS', 
'BTC_BURST', 'BTC_CLAM', 'BTC_DASH', 'BTC_DGB', 'BTC_DOGE', 'BTC_EMC2', 'BTC_FLDC', 
'BTC_FLO', 'BTC_GAME', 'BTC_GRC', 'BTC_HUC', 'BTC_LTC', 'BTC_MAID', 'BTC_OMNI', 
'BTC_NAUT', 'BTC_NAV', 'BTC_NEOS', 'BTC_NMC', 'BTC_NOTE', 'BTC_NXT', 'BTC_PINK', 
'BTC_POT', 'BTC_PPC', 'BTC_RIC', 'BTC_SJCX', 'BTC_STR', 'BTC_SYS', 'BTC_VIA', 
'BTC_XVC', 'BTC_VRC', 'BTC_VTC', 'BTC_XBC', 'BTC_XCP', 'BTC_XEM', 'BTC_XMR', 
'BTC_XPM', 'BTC_XRP', 'USDT_BTC', 'USDT_DASH', 'USDT_LTC', 'USDT_NXT', 'USDT_STR', 
'USDT_XMR', 'USDT_XRP', 'XMR_BCN', 'XMR_BLK', 'XMR_BTCD', 'XMR_DASH', 'XMR_LTC', 
'XMR_MAID', 'XMR_NXT', 'BTC_ETH', 'USDT_ETH', 'BTC_SC', 'BTC_BCY', 'BTC_EXP', 
'BTC_FCT', 'BTC_RADS', 'BTC_AMP', 'BTC_DCR', 'BTC_LSK', 'ETH_LSK', 'BTC_LBC', 
'BTC_STEEM', 'ETH_STEEM', 'BTC_SBD', 'BTC_ETC', 'ETH_ETC', 'USDT_ETC', 'BTC_REP', 
'USDT_REP', 'ETH_REP', 'BTC_ARDR', 'BTC_ZEC', 'ETH_ZEC', 'USDT_ZEC', 'XMR_ZEC', 
'BTC_STRAT', 'BTC_NXC', 'BTC_PASC', 'BTC_GNT', 'ETH_GNT', 'BTC_GNO', 'ETH_GNO']

def getOrders(pair):
    r = requests.get('https://poloniex.com/public?command=returnOrderBook&currencyPair='+pair)
    return r.json()

def topAskBid(pair):
    orders = getOrders(pair)
    ask = float(orders['asks'][0][0])
    bid = float(orders['bids'][0][0])
    return ask, bid


