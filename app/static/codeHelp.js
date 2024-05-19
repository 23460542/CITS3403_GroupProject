$(document).ready(function() {
    // Function to apply light theme
    function enableLightTheme() {
        $('body').removeClass('dark-theme');
        $('.btn2').removeClass('btn-light').addClass('btn-dark');
        $('.btn-home, .btn-ask, .btn-questions').removeClass('text-white');
        localStorage.setItem('theme', 'light');
    }

    // Function to apply dark theme
    function enableDarkTheme() {
        $('body').addClass('dark-theme');
        $('.btn2').removeClass('btn-dark').addClass('btn-light');
        $('.btn-home, .btn-ask, .btn-questions').addClass('text-white');
        localStorage.setItem('theme', 'dark');
    }

    // Handle checkbox change event
    $('#themeToggle').change(function() {
        if (this.checked) {
            enableDarkTheme();
        } else {
            enableLightTheme();
        }
    });

    // Check initial theme and apply it
    if (localStorage.getItem('theme') === 'dark') {
        $('#themeToggle').prop('checked', true);
        enableDarkTheme();
    } else {
        enableLightTheme();
    }
});

function profMenuToggle() {
    if (document.getElementById("prof-menu").className == "hidden") {
        document.getElementById("prof-menu").classList.remove("hidden");
    }
    else {
        document.getElementById("prof-menu").className = "hidden";
    }
  }