<?php

namespace OPNsense\IPAnalyzer\Api;

use \OPNsense\Base\ApiControllerBase;
use \OPNsense\Core\Backend;

class IpController extends ApiControllerBase{

    public function showAction()
    {
        $backend = new Backend();
        $bckresult = json_decode(trim($backend->configdRun("ipanalyzer show")), true);
        if ($bckresult !== null) {
            // only return valid json type responses
            return $bckresult;
        }
        return array("message" => "unable to run ipanalyzer show");
    }

    public function deleteAction()
    {
        $backend = new Backend();
        $bckresult = json_decode(trim($backend->configdRun("ipanalyzer delete")), true);
        if ($bckresult !== null) {
            // only return valid json type responses
            return $bckresult;
        }
        return array("message" => "unable to run ipanalyzer delete");
    }

    public function appendAction()
    {
        $backend = new Backend();
        $bckresult = json_decode(trim($backend->configdRun("ipanalyzer append")), true);
        if ($bckresult !== null) {
            // only return valid json type responses
            return $bckresult;
        }
        return array("message" => "unable to run ipanalyzer append");
    }

    public function stopAction()
    {
        $backend = new Backend();
        $bckresult = json_decode(trim($backend->configdRun("ipanalyzer stop")), true);
        if ($bckresult !== null) {
            // only return valid json type responses
            return $bckresult;
        }
        return array("message" => "unable to run ipanalyzer stop");
    }

}