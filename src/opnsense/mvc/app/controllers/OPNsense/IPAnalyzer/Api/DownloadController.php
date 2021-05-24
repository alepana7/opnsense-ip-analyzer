<?php

namespace OPNsense\IPAnalyzer\Api;

use \OPNsense\Base\ApiControllerBase;

class DownloadController extends ApiControllerBase{
    const PATH_HTTP_CSV = "/usr/local/opnsense/scripts/OPNsense/IPAnalyzer/http_requests.csv";

    public function csvAction() {
        $this->response->setStatusCode(200,"OK");
        $requests = file_get_contents(self::PATH_HTTP_CSV);
        $this->response->setContentType("text/csv","UTF-8");
        $this->response->setHeader("Content-Disposition","attachment; filename=\"http_requests.csv\"");
        $this->response->setContent($requests);
    }

    public function afterExecuteRoute($dispatcher){
        $this->response->send($dispatcher);
    }
}