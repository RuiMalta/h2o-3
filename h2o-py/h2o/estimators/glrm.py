#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
from __future__ import absolute_import, division, print_function, unicode_literals

import re
from h2o.estimators.estimator_base import H2OEstimator
from h2o.exceptions import H2OValueError
from h2o.frame import H2OFrame
from h2o.utils.typechecks import assert_is_type, numeric


class H2OGeneralizedLowRankEstimator(H2OEstimator):
    """
    Generalized Low Rank Modeling

    Builds a generalized low rank model of a H2O dataset.
    """

    algo = "glrm"

    def __init__(self, **kwargs):
        super(H2OGeneralizedLowRankEstimator, self).__init__()
        self._parms = {}
        names_list = {"model_id", "training_frame", "validation_frame", "ignored_columns", "ignore_const_cols",
                      "score_each_iteration", "loading_name", "transform", "k", "loss", "loss_by_col",
                      "loss_by_col_idx", "multi_loss", "period", "regularization_x", "regularization_y", "gamma_x",
                      "gamma_y", "max_iterations", "max_updates", "init_step_size", "min_step_size", "seed", "init",
                      "svd_method", "user_y", "user_x", "expand_user_y", "impute_original", "recover_svd",
                      "max_runtime_secs"}
        if "Lambda" in kwargs: kwargs["lambda_"] = kwargs.pop("Lambda")
        for pname in kwargs:
            if pname in names_list:
                # Using setattr(...) will invoke type-checking of the arguments
                setattr(self, pname, kwargs[pname])
            else:
                raise H2OValueError("Unknown parameter %s" % pname)
        self._parms["_rest_version"] = 3

    @property
    def training_frame(self):
        """str: Id of the training data frame (Not required, to allow initial validation of model parameters)."""
        return self._parms.get("training_frame")

    @training_frame.setter
    def training_frame(self, training_frame):
        assert_is_type(training_frame, None, str, H2OFrame)
        self._parms["training_frame"] = training_frame


    @property
    def validation_frame(self):
        """str: Id of the validation data frame."""
        return self._parms.get("validation_frame")

    @validation_frame.setter
    def validation_frame(self, validation_frame):
        assert_is_type(validation_frame, None, str, H2OFrame)
        self._parms["validation_frame"] = validation_frame


    @property
    def ignored_columns(self):
        """List[str]: Names of columns to ignore for training."""
        return self._parms.get("ignored_columns")

    @ignored_columns.setter
    def ignored_columns(self, ignored_columns):
        assert_is_type(ignored_columns, None, [str])
        self._parms["ignored_columns"] = ignored_columns


    @property
    def ignore_const_cols(self):
        """bool: Ignore constant columns. (Default: True)"""
        return self._parms.get("ignore_const_cols")

    @ignore_const_cols.setter
    def ignore_const_cols(self, ignore_const_cols):
        assert_is_type(ignore_const_cols, None, bool)
        self._parms["ignore_const_cols"] = ignore_const_cols


    @property
    def score_each_iteration(self):
        """bool: Whether to score during each iteration of model training. (Default: False)"""
        return self._parms.get("score_each_iteration")

    @score_each_iteration.setter
    def score_each_iteration(self, score_each_iteration):
        assert_is_type(score_each_iteration, None, bool)
        self._parms["score_each_iteration"] = score_each_iteration


    @property
    def loading_name(self):
        """str: Frame key to save resulting X"""
        return self._parms.get("loading_name")

    @loading_name.setter
    def loading_name(self, loading_name):
        assert_is_type(loading_name, None, str)
        self._parms["loading_name"] = loading_name


    @property
    def transform(self):
        """
        Enum["none", "standardize", "normalize", "demean", "descale"]: Transformation of training data (Default: "none")
        """
        return self._parms.get("transform")

    @transform.setter
    def transform(self, transform):
        transform = re.sub(r"[^a-z]+", "", transform.lower())
        assert_is_type(transform, None, "none", "standardize", "normalize", "demean", "descale")
        self._parms["transform"] = transform


    @property
    def k(self):
        """int: Rank of matrix approximation (Default: 1)"""
        return self._parms.get("k")

    @k.setter
    def k(self, k):
        assert_is_type(k, None, int)
        self._parms["k"] = k


    @property
    def loss(self):
        """
        Enum["quadratic", "absolute", "huber", "poisson", "hinge", "logistic", "periodic"]: Numeric loss function
        (Default: "quadratic")
        """
        return self._parms.get("loss")

    @loss.setter
    def loss(self, loss):
        loss = re.sub(r"[^a-z]+", "", loss.lower())
        assert_is_type(loss, None, "quadratic", "absolute", "huber", "poisson", "hinge", "logistic", "periodic")
        self._parms["loss"] = loss


    @property
    def loss_by_col(self):
        """
        List[Enum["quadratic", "absolute", "huber", "poisson", "hinge", "logistic", "periodic", "categorical",
        "ordinal"]]: Loss function by column (override)
        """
        return self._parms.get("loss_by_col")

    @loss_by_col.setter
    def loss_by_col(self, loss_by_col):
        loss_by_col = re.sub(r"[^a-z]+", "", loss_by_col.lower())
        assert_is_type(loss_by_col, None, ["quadratic", "absolute", "huber", "poisson", "hinge", "logistic", "periodic", "categorical", "ordinal"])
        self._parms["loss_by_col"] = loss_by_col


    @property
    def loss_by_col_idx(self):
        """List[int]: Loss function by column index (override)"""
        return self._parms.get("loss_by_col_idx")

    @loss_by_col_idx.setter
    def loss_by_col_idx(self, loss_by_col_idx):
        assert_is_type(loss_by_col_idx, None, [int])
        self._parms["loss_by_col_idx"] = loss_by_col_idx


    @property
    def multi_loss(self):
        """Enum["categorical", "ordinal"]: Categorical loss function (Default: "categorical")"""
        return self._parms.get("multi_loss")

    @multi_loss.setter
    def multi_loss(self, multi_loss):
        multi_loss = re.sub(r"[^a-z]+", "", multi_loss.lower())
        assert_is_type(multi_loss, None, "categorical", "ordinal")
        self._parms["multi_loss"] = multi_loss


    @property
    def period(self):
        """int: Length of period (only used with periodic loss function) (Default: 1)"""
        return self._parms.get("period")

    @period.setter
    def period(self, period):
        assert_is_type(period, None, int)
        self._parms["period"] = period


    @property
    def regularization_x(self):
        """
        Enum["none", "quadratic", "l2", "l1", "non_negative", "one_sparse", "unit_one_sparse", "simplex"]:
        Regularization function for X matrix (Default: "none")
        """
        return self._parms.get("regularization_x")

    @regularization_x.setter
    def regularization_x(self, regularization_x):
        regularization_x = re.sub(r"[^a-z]+", "", regularization_x.lower())
        assert_is_type(regularization_x, None, "none", "quadratic", "l", "l", "nonnegative", "onesparse", "unitonesparse", "simplex")
        self._parms["regularization_x"] = regularization_x


    @property
    def regularization_y(self):
        """
        Enum["none", "quadratic", "l2", "l1", "non_negative", "one_sparse", "unit_one_sparse", "simplex"]:
        Regularization function for Y matrix (Default: "none")
        """
        return self._parms.get("regularization_y")

    @regularization_y.setter
    def regularization_y(self, regularization_y):
        regularization_y = re.sub(r"[^a-z]+", "", regularization_y.lower())
        assert_is_type(regularization_y, None, "none", "quadratic", "l", "l", "nonnegative", "onesparse", "unitonesparse", "simplex")
        self._parms["regularization_y"] = regularization_y


    @property
    def gamma_x(self):
        """float: Regularization weight on X matrix (Default: 0.0)"""
        return self._parms.get("gamma_x")

    @gamma_x.setter
    def gamma_x(self, gamma_x):
        assert_is_type(gamma_x, None, numeric)
        self._parms["gamma_x"] = gamma_x


    @property
    def gamma_y(self):
        """float: Regularization weight on Y matrix (Default: 0.0)"""
        return self._parms.get("gamma_y")

    @gamma_y.setter
    def gamma_y(self, gamma_y):
        assert_is_type(gamma_y, None, numeric)
        self._parms["gamma_y"] = gamma_y


    @property
    def max_iterations(self):
        """int: Maximum number of iterations (Default: 1000)"""
        return self._parms.get("max_iterations")

    @max_iterations.setter
    def max_iterations(self, max_iterations):
        assert_is_type(max_iterations, None, int)
        self._parms["max_iterations"] = max_iterations


    @property
    def max_updates(self):
        """int: Maximum number of updates (Default: 2000)"""
        return self._parms.get("max_updates")

    @max_updates.setter
    def max_updates(self, max_updates):
        assert_is_type(max_updates, None, int)
        self._parms["max_updates"] = max_updates


    @property
    def init_step_size(self):
        """float: Initial step size (Default: 1.0)"""
        return self._parms.get("init_step_size")

    @init_step_size.setter
    def init_step_size(self, init_step_size):
        assert_is_type(init_step_size, None, numeric)
        self._parms["init_step_size"] = init_step_size


    @property
    def min_step_size(self):
        """float: Minimum step size (Default: 0.0001)"""
        return self._parms.get("min_step_size")

    @min_step_size.setter
    def min_step_size(self, min_step_size):
        assert_is_type(min_step_size, None, numeric)
        self._parms["min_step_size"] = min_step_size


    @property
    def seed(self):
        """int: RNG seed for initialization (Default: -1)"""
        return self._parms.get("seed")

    @seed.setter
    def seed(self, seed):
        assert_is_type(seed, None, int)
        self._parms["seed"] = seed


    @property
    def init(self):
        """Enum["random", "svd", "plus_plus", "user"]: Initialization mode (Default: "plus_plus")"""
        return self._parms.get("init")

    @init.setter
    def init(self, init):
        init = re.sub(r"[^a-z]+", "", init.lower())
        assert_is_type(init, None, "random", "svd", "plusplus", "user")
        self._parms["init"] = init


    @property
    def svd_method(self):
        """
        Enum["gram_s_v_d", "power", "randomized"]: Method for computing SVD during initialization (Caution: Power and
        Randomized are currently experimental and unstable) (Default: "randomized")
        """
        return self._parms.get("svd_method")

    @svd_method.setter
    def svd_method(self, svd_method):
        svd_method = re.sub(r"[^a-z]+", "", svd_method.lower())
        assert_is_type(svd_method, None, "gramsvd", "power", "randomized")
        self._parms["svd_method"] = svd_method


    @property
    def user_y(self):
        """str: User-specified initial Y"""
        return self._parms.get("user_y")

    @user_y.setter
    def user_y(self, user_y):
        assert_is_type(user_y, None, str, H2OFrame)
        self._parms["user_y"] = user_y


    @property
    def user_x(self):
        """str: User-specified initial X"""
        return self._parms.get("user_x")

    @user_x.setter
    def user_x(self, user_x):
        assert_is_type(user_x, None, str, H2OFrame)
        self._parms["user_x"] = user_x


    @property
    def expand_user_y(self):
        """bool: Expand categorical columns in user-specified initial Y (Default: True)"""
        return self._parms.get("expand_user_y")

    @expand_user_y.setter
    def expand_user_y(self, expand_user_y):
        assert_is_type(expand_user_y, None, bool)
        self._parms["expand_user_y"] = expand_user_y


    @property
    def impute_original(self):
        """bool: Reconstruct original training data by reversing transform (Default: False)"""
        return self._parms.get("impute_original")

    @impute_original.setter
    def impute_original(self, impute_original):
        assert_is_type(impute_original, None, bool)
        self._parms["impute_original"] = impute_original


    @property
    def recover_svd(self):
        """bool: Recover singular values and eigenvectors of XY (Default: False)"""
        return self._parms.get("recover_svd")

    @recover_svd.setter
    def recover_svd(self, recover_svd):
        assert_is_type(recover_svd, None, bool)
        self._parms["recover_svd"] = recover_svd


    @property
    def max_runtime_secs(self):
        """float: Maximum allowed runtime in seconds for model training. Use 0 to disable. (Default: 0.0)"""
        return self._parms.get("max_runtime_secs")

    @max_runtime_secs.setter
    def max_runtime_secs(self, max_runtime_secs):
        assert_is_type(max_runtime_secs, None, numeric)
        self._parms["max_runtime_secs"] = max_runtime_secs


