<?php

namespace OPNsense\IPAnalyzer;

class IndexController extends \OPNsense\Base\IndexController {
    public function indexAction() {
        $this->view->pick('OPNsense/IPAnalyzer/index');
        $this->view->generalForm = $this->getForm("general");
    }
}
?>
