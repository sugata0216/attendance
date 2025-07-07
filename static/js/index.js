$(function() {
  $('.hamburger').click(function() {
    $('.menu').toggleClass('open');
    $(this).toggleClass('active');
  });
});