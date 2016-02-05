# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Utility function to manage CLI entry points"""

import traceback

import click
import pkg_resources


def open_entry_point(group_name):
    """Open entry point."""
    def loader(dummy_ctx, param, value):
        """Load entry point from group name based on given value."""
        entry_points = list(pkg_resources.iter_entry_points(
            group_name, value
        ))
        assert len(entry_points) == 1
        return entry_points[0].load()
    return loader


def with_plugins(group_name):
    """Register external CLI commands."""
    def decorator(group):
        """Attach loaded commands to the group."""
        if not isinstance(group, click.Group):
            raise TypeError(
                'Plugins can only be attached to an instance of click.Group.'
            )
        for entry_point in pkg_resources.iter_entry_points(group_name):
            try:
                group.add_command(entry_point.load())
            except Exception:
                click.echo('Command {0} could not be loaded. \n\n{1}'.format(
                    entry_point.name, traceback.format_exc()
                ))
        return group
    return decorator
