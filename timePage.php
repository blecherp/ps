<?php echo file_get_contents("General/header.html"); ?>

<?php echo file_get_contents("General/staticItems.html"); ?>
<?php echo file_get_contents("General/sidebarFilters.html"); ?>




<div id="mainContentContainer" class="container-fluid" style="margin-top: 4mm;">

    <!-- Start: Enter content here! -->



    <div class="row">
		<div class="col-md-8 offset-md-2">
            <h2>Timeline</h2>
            <div class="container-fluid">

                <div class="row" style="margin-bottom: 2mm">
                    <div class="card" style="width: 100%">
                        <div class="card-body">
                            <h5 class="card-title">Server</h5>
                            <h6 class="card-subtitle mb-2 text-muted">12:00:00</h6>
                            <p class="card-text">User "Nils" joined the server</p>
                        </div>
                    </div>
                </div>

                <div class="row" style="margin-bottom: 2mm">
                    <div class="card" style="width: 100%">
                        <div class="card-body">
                            <h5 class="card-title">Server</h5>
                            <h6 class="card-subtitle mb-2 text-muted">12:03:27</h6>
                            <p class="card-text">User "Ole" joined the server</p>
                        </div>
                    </div>
                </div>

                <div class="row" style="margin-bottom: 2mm">
                    <div class="card" style="width: 100%">
                        <div class="card-body">
                            <h5 class="card-title">Drawing</h5>
                            <h6 class="card-subtitle mb-2 text-muted">12:08:06</h6>
                            <p class="card-text">User "Nils" made a drawing</p>
                            <div id="accordion">

                                <h5 class="mb-0" id="headingOne">
                                    <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                                    Show drawing
                                    </button>
                                </h5>
                                

                                <div id="collapseOne" class="collapse hide" aria-labelledby="headingOne" data-parent="#accordion">
                                    <img src="Images/Drawing1.png" alt="..." class="img-thumbnail">
                                </div>

                            </div>
                            
                        </div>
                    </div>
                </div>


            </div>

		</div>
	</div>


    <!-- End: Enter content here! -->

</div>

<?php echo file_get_contents("General/footer.html"); ?>