<?php

namespace OPNsense\IPAnalyzer\Api;

use \OPNsense\Base\ApiMutableModelControllerBase;

class SettingsController extends ApiMutableModelControllerBase{

    protected static $internalModelName = 'ipanalyzer';
    protected static $internalModelClass = 'OPNsense\IPAnalyzer\IPAnalyzer';

}