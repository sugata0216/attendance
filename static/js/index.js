$(function () {
  $('.hamburger').click(function () {
    $('.menu').toggleClass('open');
    $(this).toggleClass('active');
  });
});
document.addEventListener('DOMContentLoaded', function () {
  const calendarEl = document.getElementById('calendar');
  const url = calendarEl.dataset.url;
  const csrfToken = calendarEl.dataset.csrf;

  const calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'timeGridWeek',
    allDaySlot: false,
    slotMinTime: '09:30:00',
    slotMaxTime: '16:50:00',
    slotDuration: '01:30:00',
    locale: 'ja',
    firstDay: 1,
    headerToolbar: {
      left: 'prev,next',
      center: 'title',
      right: 'timeGridWeek,timeGridDay'
    },
    slotLabelFormat: {
      hour: '2-digit',
      minute: '2-digit',
      hour12: false
    },
   datesSet() {
      setTimeout(addPeriodLabels, 10);
    },
    viewDidMount() {
      setTimeout(addPeriodLabels, 10);
    },
    dateClick: function (info) {
      $.ajax({
        url: url,
        type: 'POST',
        data: {
          date: info.dateStr,
          student_id: 1,
          subject_id: 1,
          status: 'present',
          csrfmiddlewaretoken: csrfToken
        },
        success: function () {
          alert("出席を登録しました: " + info.dateStr);
        },
        error: function () {
          alert("エラーが発生しました");
        }
      });
    }
  });

  calendar.render();

  function addPeriodLabels() {
  console.log('addPeriodLabels呼ばれた');
  const labels = ['1限目', '2限目', '3限目', '4限目'];
  const labelEls = document.querySelectorAll('.fc-timegrid-slot-label-cushion.fc-scrollgrid-shrink-cushion');
  labelEls.forEach((el, i) => {
    if (i < labels.length) {
      el.textContent = labels[i];
    } else {
      el.textContent = '';
    }
  });
}
  });
;