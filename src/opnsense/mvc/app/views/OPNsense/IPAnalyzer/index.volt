<div class="content-box">
    <h1>IP Analyzer<h1>
    <h2>This plugins filters all IP requests inside your LAN<h2>
</div>
<div class="content-box">
    <div class="col-md-12">
        {{ partial("layout_partials/base_form",['fields':generalForm,'id':'frm_GeneralSettings'])}}
    </div>
</div>
<div class="content-box">
    <table id="log-table" class="table table-condensed">
         <thead>
              <tr>
                <th>
                    <a href="/api/ipanalyzer/download/csv">
                        <button class="btn btn-primary" id="log-report" type="button">
                            <b>{{ lang._('Export Log') }}</b>
                        </button>
                    </a>
                </th>
                <th>
                    <button class="btn btn-primary" id="log-delete" type="button">
                        <b>{{ lang._('Delete Log') }}</b>
                    </button>
                </th>
                <th>
                    <button class="btn btn-primary" id="log-append" type="button">
                        <b>{{ lang._('Detect bad IPs requests') }}</b>
                    </button>
                </th>
                <th>
                    <button class="btn btn-primary" id="log-stop" type="button">
                        <b>{{ lang._('Stop detecting bad IPs requests') }}</b>
                    </button>
                </th>
              </tr>
             <tr id="log-header">
                         <td data-column-id="DateTime" class="text-left" style="width:4em;" >DateTime (UTC)</td>
                         <td data-column-id="IP src" class="text-left" style="width:4em;" >Id</td>
                         <td data-column-id="IP src" class="text-left" style="width:4em;" >Src Eth</td>
                         <td data-column-id="IP src" class="text-left" style="width:4em;" >IP src</td>
                         <td data-column-id="IP src" class="text-left" style="width:4em;" >Dest Eth</td>
                         <td data-column-id="IP dest" class="text-left" style="width:4em;" >IP dest</td>
                         <td data-column-id="Port src" class="text-left" style="width:4em;" >Port src</td>
                         <td  data-column-id="Port dest" class="text-left" style="width:4em;" >Port dest</td>
                         <td  data-column-id="Port dest" class="text-left" style="width:4em;" >Nature</td>
             </tr>
           </thead>
           <tbody id="log-body">
           </tbody>
    </table>
</div>
<div>
    <button class="btn btn-primary" id="save-settings" type="button">
        <b>{{ lang._('Save configuration') }}</b>
    </button>
</div>

<script type="text/javascript">

    function show_log(){
        ajaxCall(url="/api/ipanalyzer/ip/show",sendData={},callback = function(data,status){
             if(data.length === 0){
                let str = "<p class='text-center' >No packets found</p>";
                 $("#log-body").html(str);
             }
             else{
                let obj ="";
                for(const i = 0; i < data.length; i++){
                     obj +=
                     "<tr>" +
                     "<td class='text-left'>" + data[i][0] + "</td>" +
                     "<td class='text-left'>" + data[i][1] + "</td>" +
                     "<td class='text-left'>" + data[i][2] + "</td>" +
                     "<td class='text-left'>" + data[i][3] + "</td>" +
                     "<td class='text-left'>" + data[i][4] + "</td>" +
                     "<td class='text-left'>" + data[i][5] + "</td>" +
                     "<td class='text-left'>" + data[i][6] + "</td>" +
                     "<td class='text-left'>" + data[i][7] + "</td>" +
                     "<td class='text-left'>" + data[i][8] + "</td>" +
                     "</tr>";
                 }
                 $("#log-body").html(obj);
                 }
        });
    }

    $( document ).ready(function() {
        var data_get_map = {'frm_GeneralSettings':"/api/ipanalyzer/settings/get/"};
         mapDataToFormUI(data_get_map).done(function(data){
         });
         show_log();
     });

      $( "#save-settings" ).click(function(){
            saveFormToEndpoint(url="/api/ipanalyzer/settings/set/",formid='frm_GeneralSettings',callback_ok=function(){
              // action to run after successful save, for example reconfigure service.
             ajaxCall(url="/api/ipanalyzer/service/reload/", sendData={},callback=function(data,status) {
              });
           });
              show_log();
        });


      $( "#log-delete" ).click(function(){
        ajaxCall(url="/api/ipanalyzer/ip/delete/", sendData={},callback=function(data,status) {

        });
        $( "#log-body" ).html("");
     });

    $( "#log-append" ).click(function(){
        ajaxCall(url="/api/ipanalyzer/ip/append/", sendData={},callback=function(data,status) {
        });
        show_log();
    });

    $( "#log-stop" ).click(function(){
        ajaxCall(url="/api/ipanalyzer/ip/stop/", sendData={},callback=function(data,status) {
        });
    });

</script>