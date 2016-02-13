import os
from fxpt.side_utils import yaml

from fxpt.fx_utils import message_box
from fxpt.fx_utils.utils import makeWritable


def load(filename, silent=False):
    try:
        with open(filename, 'r') as f:
            obj = yaml.load(f)
    except IOError:
        if not silent:
            if not os.path.exists(filename):
                message_box.exception('Cannot load YAML file. File does not exists:\n{}'.format(filename))
            else:
                message_box.exception('Cannot load YAML file:\n{}'.format(filename))
        raise
    except yaml.YAMLError:
        if not silent:
            message_box.exception('Error parsing YAML file. Check syntax:\n{}'.format(filename))
        raise
    except StandardError:
        if not silent:
            message_box.exception('Unexpected error loading YAML file:\n{}'.format(filename))
        raise

    return obj


def dump(filename, obj, silent=False):
    try:
        makeWritable(filename)
        with open(filename, 'w') as f:
            f.write(yaml.dump(obj, default_flow_style=False))
    except IOError:
        if not silent:
            message_box.exception('Cannot save YAML file:\n{}'.format(filename))
        raise
    except StandardError:
        if not silent:
            message_box.exception('Unexpected error saving YAML file:\n{}'.format(filename))
        raise

