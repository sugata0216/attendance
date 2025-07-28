$(function () {
  $('.hamburger').click(function () {
    $('.menu').toggleClass('open');
    $(this).toggleClass('active');
  });
});
function roundToNearestPeriodStart(timestr) {
  const periodStarts = ["09:30", "11:00", "12:30", "14:00"];
  const timeMinutes = timeStrToMinutes(timestr);
  let closest = periodStarts[0];
  let closestDiff = Math.abs(timeMinutes - timeStrToMinutes(closest));
  for (const start of periodStarts) {
    const diff = Math.abs(timeMinutes - timeStrToMinutes(start));
    if (diff < closestDiff) {
      closest = start;
      closestDiff = diff;
    }
  }  
  return closest;
}
function timeStrToMinutes(timestr) {
  const [h, m] = timestr.split(':').map(Number);
  return h * 60 + m;
}
function getPeriodFromTime(timestr) {
  const periods = [
    {period: 1, start: "09:30", end: "11:00"},
    {period: 2, start: "11:00", end: "12:30"},
    {period: 3, start: "12:30", end: "14:00"},
    {period: 4, start: "14:00", end: "15:30"},
  ];
  const timeMin = timeStrToMinutes(timestr);
  for (const p of periods) {
    const startMin = timeStrToMinutes(p.start);
    const endMin = timeStrToMinutes(p.end);
    if (timeMin >= startMin && timeMin < endMin) {
      return p.period;
    }
  }
  return null;
}
document.addEventListener('DOMContentLoaded', function () {
  const calendarEl = document.getElementById('calendar');
  const url = calendarEl.dataset.url;
  const csrfToken = calendarEl.dataset.csrf;

  const calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'timeGridWeek',
    allDaySlot: false,
    slotMinTime: '09:30:00',
    slotMaxTime: '15:30:00',
    slotDuration: '01:30:00',
    slotLabelInterval: '01:30:00',
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
    slotLabelContent: function(arg) {
    const hour = arg.date.getHours();
    const minute = arg.date.getMinutes();
    const timeStr = `${hour.toString().padStart(2, '0')}:${minute.toString().padStart(2, '0')}`;
    
    const labels = {
      "09:30": "1限目",
      "11:00": "2限目",
      "12:30": "3限目",
      "14:00": "4限目"
    };

    if (labels[timeStr]) {
      return { html: labels[timeStr] };
    }
    return { html: '' }; // その他の時間は表示しない
  },
  //  datesSet() {
  //     setTimeout(addPeriodLabels, 10);
  //   },
  //   viewDidMount() {
  //     setTimeout(addPeriodLabels, 10);
  //   },
    dateClick: function (info) {
      console.log("Clicked:", info.dateStr);
      const date = new Date(info.dateStr);
      const hour = date.getHours();
      const minute = date.getMinutes();
      const timestr = `${hour.toString().padStart(2, '0')}:${minute.toString().padStart(2, '0')}`;
      console.log("時刻:", timestr);
      const rounded = roundToNearestPeriodStart(timestr);
      const period = getPeriodFromTime(rounded);
      console.log("period:", period);
      if (period === null) {
        alert("有効な時間帯を選択してください。");
        return;
      }
      const dateOnlyStr = info.dateStr.split("T")[0];
      const url = `/attendance_management/create/${dateOnlyStr}/${period}/`;
      window.location.href = url;
      },
    eventSources: [
      {
        url: '/attendance_management/get_events/', 
        method: 'GET',
        extraParams: function() {
          return {
            csrfmiddlewaretoken: csrfToken
          };
        },
        failure: function() {
          alert('イベントの読み込みに失敗しました。');
        }
      }
    ],
    eventDidMount: function(info) {
      const period = getPeriodFromTime(info.event.start.toTimeString().slice(0, 5));
      if (period !== null) {
        info.el.classList.add(`period-${period}`);
      }
    }
  });

  calendar.render();
});
const toggleBtn = document.getElementById("darkModeToggle");
const body = document.body;
toggleBtn.addEventListener("click", function() {
  body.classList.toggle("dark-mode");
  if (body.classList.contains("dark-mode")) {
    localStorage.setItem("theme", "dark");
  } else {
    localStorage.setItem("theme", "light");
  }
});
window.addEventListener("DOMContentLoaded", function() {
  if (this.localStorage.getItem("theme") === "dark") {
    body.classList.add("dark-mode");
  }
});