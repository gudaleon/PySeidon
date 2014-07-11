#!/usr/bin/python2.7
# encoding: utf-8

import numpy as np

class Functions:
    ''' '''
    def __init__(self,cls):
        self._var = cls.Variables
        self._grid = cls.Grid
        self._ax = cls._ax
    
    def el_region(self):

        region_e = np.argwhere((self._var.lonc >= self._ax[0]) &
                                     (self._var.lonc <= self._ax[1]) &
                                     (self._var.latc >= self._ax[2]) &
                                     (self._var.latc <= self._ax[3]))

        return region_e

    def node_region(self):

        region_n = np.argwhere((self._var.lon >= self._ax[0]) &
                                     (self._var.lon <= self._ax[1]) &
                                     (self._var.lat >= self._ax[2]) &
                                     (self._var.lat <= self._ax[3]))

        return region_n

    def centers(self):
        size = self._grid.trinodes.T.shape[0]
        size1 = self._var.el.shape[0]
        elc = np.zeros((size1, size))
        hc = np.zeros((size))
        for i,v in enumerate(self._grid.trinodes.T):
            elc[:, i] = np.mean(self._var.el[:, v], axis=1)
            hc[i] = np.mean(self._var.h[v], axis=1)

        return elc, hc

    def hc(self):
        size = self._grid.trinodes.T.shape[0]
        size1 = self._var.el.shape[0]
        elc = np.zeros((size1, size))
        for i,v in enumerate(self._grid.trinodes.T):
            elc[:, i] = np.mean(self._var.el[:, v], axis=1)

    def closest_point(self, pt_lon, pt_lat):
    # def closest_point(self, pt_lon, pt_lat, lon, lat):
        '''
        Finds the closest exact lon, lat to a lon, lat coordinate.
        Example input:
            closest_point([-65.37], [45.34], lon, lat)

        where lon, lat are from data
        '''

        points = np.array([pt_lon, pt_lat]).T

        #point_list = np.array([lon,lat]).T
        point_list = np.array([self._var.lonc, self._var.latc]).T

        closest_dist = ((point_list[:, 0] - points[:, 0, None])**2 +
                        (point_list[:, 1] - points[:, 1, None])**2)

        closest_point_indexes = np.argmin(closest_dist, axis=1)

        return closest_point_indexes

