(function($){
  var wrap = $("#wrap");
  wrap.on("scroll", function(e)
  {
    if (this.scrollTop > 147)
    {
      wrap.addClass("fix-search");
    }
    else
    {
      wrap.removeClass("fix-search");
    }
  });
  $(document).ready(function()
  {
    $('.scrollspy').scrollSpy();
    $('.button-collapse').sideNav();
    $('.parallax').parallax();
    $('.dropdown-button').dropdown
    ({
      inDuration: 300,
      outDuration: 225,
      constrain_width: false, // Does not change width of dropdown to that of the activator
      hover: true, // Activate on hover
      gutter: 0, // Spacing from edge
      belowOrigin: true  // Displays dropdown below the button
    });
  }); // end of document ready
})(jQuery); // end of jQuery name space