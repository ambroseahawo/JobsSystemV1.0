$(document).ready(function(e){
    $('.search-panel .dropdown-menu').find('a').click(function(e) {
		e.preventDefault();
		var param = $(this).attr("href").replace("#","");
		var concept = $(this).text();
		$('.search-panel span#search_concept').text(concept);
		$('.input-group #search_param').val(param);
	});
});

$(".see_more").show();
$(".details").hide();

function see_more(job_id, section, event){
    event.preventDefault();

    if (section == 'req'){
        var see_more_req = "#see-more-req" + job_id;
        var requirements = "#req" + job_id;
        $(see_more_req).toggle();
        $(requirements).toggle();
    }else if(section == 'about'){
        var see_more_about = "#see-more-about" + job_id;
        var about = "#about" + job_id;

        $(see_more_about).toggle();
        $(about).toggle();
    }
}

$("#complete_profile").hide();
$("#dp_form").hide();
$("#experiences_toggle").hide();
$("#experiences_table").show();
$("#interests_toggle").hide();
$("#interests_table").show();
$("#education_toggle").hide();
$("#education_table").show();
$("#skills_toggle").hide();
$("#skills_table").show();

$("#change_dp").click(function () {
    $("#dp_form").toggle();
});

$("#update_profile").click(function () {
    $("#complete_profile").toggle();
});

$("#submit_profile").click(function () {
    $("#complete_profile").toggle();
});

$("#add_experience").click(function () {
    $("#experiences_table").toggle();
    $("#experiences_toggle").toggle();
});

$("#add_interests").click(function () {
    $("#interests_table").toggle();
    $("#interests_toggle").toggle();
});

$("#add_education").click(function () {
    $("#education_table").toggle();
    $("#education_toggle").toggle();
});

$("#add_skills").click(function () {
    $("#skills_table").toggle();
    $("#skills_toggle").toggle();
});

$("#cancel_experience").click(function () {
    $("#experiences_table").toggle();
    $("#experiences_toggle").toggle();
});

$("#cancel_interests").click(function () {
    $("#interests_table").toggle();
    $("#interests_toggle").toggle();
});

$("#cancel_education").click(function () {
    $("#education_table").toggle();
    $("#education_toggle").toggle();
});

$("#cancel_skills").click(function () {
    $("#skills_table").toggle();
    $("#skills_toggle").toggle();
});

$("#cancel_update_profile").click(function () {
    $("#complete_profile").toggle();
});

$("#cancel_complete_profile").click(function () {
    $("#complete_profile").toggle();
});

$("#experience_form").submit(function (event) {
    event.preventDefault();

    var url = $(this).attr("action");
    var posting = $.post(url, $(this).serialize());

    posting.done(function () {
        var table = $("#experiences_table");
        table.load(" #experiences_table");
        $("#experiences_toggle").toggle();
        table.toggle();
    });
});

$("#interests_form").submit(function (event) {
    event.preventDefault();

    var url = $(this).attr("action");
    var posting = $.post(url, $(this).serialize());

    posting.done(function () {
        var table = $("#interests_table");
        table.load(" #interests_table");
        $("#interests_toggle").toggle();
        table.toggle();
    });
});

$("#education_form").submit(function (event) {
    event.preventDefault();

    var url = $(this).attr("action");
    var posting = $.post(url, $(this).serialize());

    posting.done(function () {
        var table = $("#education_table");
        table.load(" #education_table");
        $("#education_toggle").toggle();
        table.toggle();
    });
});

$("#skills_form").submit(function (event) {
    event.preventDefault();

    var url = $(this).attr("action");
    var posting = $.post(url, $(this).serialize());

    posting.done(function () {
        var table = $("#skills_table");
        table.load(" #skill_table");
        $("#skills_toggle").toggle();
        table.toggle();
    });
});

function del_experience (url){

    $.ajax({
        url: url,

        success: function () {
            var table = $("#experiences_table");
            table.load(" #experiences_table");
        },
    });
}

function del_interest (url){

    $.ajax({
        url: url,
        success: function () {
            var table = $("#interests_table");
            table.load(" #interests_table");
        },
    });
}

function del_education (url){

    $.ajax({
        url: url,
        success: function () {
            var table = $("#education_table");
            table.load(" #education_table");
        },
    });
}

function del_skill (url){

    $.ajax({
        url: url,
        success: function () {
            var table = $("#skills_table");
            table.load(" #skills_table");
        },
    });
}

$(function() {

    $('#login-form-link').click(function(e) {
		$("#login-form").delay(100).fadeIn(100);
 		$("#register-form").fadeOut(100);
		$('#register-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});
	$('#register-form-link').click(function(e) {
		$("#register-form").delay(100).fadeIn(100);
 		$("#login-form").fadeOut(100);
		$('#login-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});

});

function shortlist_job (url, job_id){
    var shortlist_btn = "#shortlist" + job_id;
    var shortlist_btn_load = " #shortlist" + job_id;

    $.ajax({
        url: url,
        success: function (data) {
            console.log(data);
            $(shortlist_btn).load(shortlist_btn_load);
        },
    });
}

