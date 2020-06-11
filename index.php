<?php echo file_get_contents("General/header.html"); ?>

<?php echo file_get_contents("General/staticItems.html"); ?>
<?php echo file_get_contents("General/sidebarNoFilters.html"); ?>


<div id="mainContentContainer" class="container-fluid" style="margin-top: 4mm;">

  <!-- Start: Enter content here! -->


  <div class="row">
    <h1 class="h2">Overview</h1>
  </div>

  <hr>

  <!-- Sample Cards -->
  <div class="row">

    <!-- Number of Users Card -->
    <div class="col-xl-3 col-md-6 mb-4">
      <div class="card border-left-primary shadow h-100 py-2">
        <div class="card-body">
          <div class="row no-gutters align-items-center">
            <div class="col mr-2">
              <div class="text-xs font-weight-bold text-primary text-uppercase mb-1">Number Of Users</div>
              <div class="h5 mb-0 font-weight-bold text-gray-800">3</div>
            </div>
            <div class="col-auto">
              <i class="fas fa-calendar fa-2x text-gray-300"></i>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Time on Server Card -->
    <div class="col-xl-3 col-md-6 mb-4">
      <div class="card border-left-primary shadow h-100 py-2">
        <div class="card-body">
          <div class="row no-gutters align-items-center">
            <div class="col mr-2">
              <div class="text-xs font-weight-bold text-primary text-uppercase mb-1">Time On Server</div>
              <div class="h5 mb-0 font-weight-bold text-gray-800">01:12:33 h</div>
            </div>
            <div class="col-auto">
              <i class="fas fa-calendar fa-2x text-gray-300"></i>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Images Drawn Card -->
    <div class="col-xl-3 col-md-6 mb-4">
      <div class="card border-left-primary shadow h-100 py-2">
        <div class="card-body">
          <div class="row no-gutters align-items-center">
            <div class="col mr-2">
              <div class="text-xs font-weight-bold text-primary text-uppercase mb-1">Images Drawn</div>
              <div class="h5 mb-0 font-weight-bold text-gray-800">17</div>
            </div>
            <div class="col-auto">
              <i class="fas fa-calendar fa-2x text-gray-300"></i>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Objects Spawned -->
    <div class="col-xl-3 col-md-6 mb-4">
      <div class="card border-left-primary shadow h-100 py-2">
        <div class="card-body">
          <div class="row no-gutters align-items-center">
            <div class="col mr-2">
              <div class="text-xs font-weight-bold text-primary text-uppercase mb-1">Objects Spawned</div>
              <div class="h5 mb-0 font-weight-bold text-gray-800">15</div>
            </div>
            <div class="col-auto">
              <i class="fas fa-calendar fa-2x text-gray-300"></i>
            </div>
          </div>
        </div>
      </div>
    </div> 

  </div>

  <!-- Sample Charts-->
  <div class="row">
    
    <!-- Pie Chart -->
    <div class="col-4">
      <div class="card shadow mb-4">
        <!-- Card Header - Dropdown -->
        <div class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
          <h6 class="m-0 font-weight-bold text-primary">Activities</h6>
        </div>
        <!-- Card Body -->
        <div class="card-body">
          <div id="donutchart"></div>
        </div>
      </div>
    </div>

    <!-- Pie Chart -->
    <div class="col-8">
      <div class="card shadow mb-4">
        <!-- Card Header - Dropdown -->
        <div class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
          <h6 class="m-0 font-weight-bold text-primary">Time On Server</h6>
        </div>
        <!-- Card Body -->
        <div class="card-body">
          <div id="timeline"></div>
        </div>
      </div>
    </div>

  </div>





  <!-- Java Script Elements -->
  <!-- Google Charts-->
  <script src="https://www.gstatic.com/charts/loader.js"></script>
  <!-- Pie Chart -->
  <script type="text/javascript">
    google.charts.load("current", {packages:["corechart"]});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
      var data = google.visualization.arrayToDataTable([
        ['Event', 'Occurence'],
        ['Chatting',     29],
        ['Drawing',     17],
        ['Creating Objects',     15],
        ['Writing',     8],
      ]);

      var options = {
        legend: {position: 'bottom'},
        pieHole: 0.3,
      };

      var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
      chart.draw(data, options);
    }
  </script>
  <!-- Timeline -->
  <script type="text/javascript">
    google.charts.load('current', {'packages':['timeline']});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
      var container = document.getElementById('timeline');
      var chart = new google.visualization.Timeline(container);
      var dataTable = new google.visualization.DataTable();

      dataTable.addColumn({ type: 'string', id: 'User' });
      dataTable.addColumn({ type: 'date', id: 'Start' });
      dataTable.addColumn({ type: 'date', id: 'End' });
      dataTable.addRows([
        [ 'Nils', new Date(0,0,0,12,0,0), new Date(0,0,0,13,7,15) ],
        [ 'Ole',      new Date(0,0,0,12,3,27),  new Date(0,0,0,12,58,7) ],
        [ 'Johanna',  new Date(0,0,0,12,35,3),  new Date(0,0,0,13,12,33) ]]);

      chart.draw(dataTable);
    }
  </script>

<!-- End: Enter content here! -->

</div>

<?php echo file_get_contents("General/footer.html"); ?>