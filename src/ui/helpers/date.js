export const defaultLang = {
  months: {
    full: [
      'Enero',
      'Febrero',
      'Marzo',
      'Abril',
      'Mayo',
      'Junio',
      'Julio',
      'Agosto',
      'Septiembre',
      'Octubre',
      'Noviembre',
      'Diciembre'
    ],
    abbreviated: [
      'Ene',
      'Feb',
      'Mar',
      'Abr',
      'May',
      'Jun',
      'Jul',
      'Ago',
      'Sep',
      'Oct',
      'Nov',
      'Dic'
    ]
  },

  days: {
    full: [
      'Domingo',
      'Lunes',
      'Martes',
      'Miércoles',
      'Jueves',
      'Viernes',
      'Sábado'
    ],

    abbreviated: [
      'Dom',
      'Lun',
      'Mar',
      'Mie',
      'Jue',
      'Vier',
      'Sat'
    ],

    initials: [
      'Do',
      'Lu',
      'Ma',
      'Mi',
      'Ju',
      'Vi',
      'Sa'
    ]
  }
}

function pad (value, length) {
  while (value.length < length) {
    value = '0' + value
  }
  return value
}

export function getDayFull (date, lang = defaultLang) {
  return lang.days.full[date.getDay()]
}

export function getDayInitial (date, lang = defaultLang) {
  return lang.days.initials[date.getDay()]
}

export function getDayAbbreviated (date, lang = defaultLang) {
  return lang.days.abbreviated[date.getDay()]
}

export function getMonthFull (date, lang = defaultLang) {
  return lang.months.full[date.getMonth()]
}

export function getMonthAbbreviated (date, lang = defaultLang) {
  return lang.months.abbreviated[date.getMonth()]
}

export function getDayOfMonth (date, options = { pad: true }) {
  const day = date.getDate().toString()
  return options.pad ? pad(day) : day
}

export function humanize (date, lang = defaultLang) {
  const days = lang.days.abbreviated
  const months = lang.months.full

  return days[date.getDay()] + ', ' + months[date.getMonth()] + ' ' + date.getDate() + ', ' + date.getFullYear()
}

export function clone (date) {
  return new Date(date.getTime())
}

export function moveToDayOfWeek (date, dayOfWeek) {
  while (date.getDay() !== dayOfWeek) {
    date.setDate(date.getDate() - 1);
  }

  return date
}

export function isSameDay (date1, date2) {
  return date1.getFullYear() === date2.getFullYear() &&
      date1.getMonth() === date2.getMonth() &&
      date1.getDate() === date2.getDate()
}

export function isBefore (date1, date2) {
  return date1.getTime() < date2.getTime()
}

export function isAfter (date1, date2) {
  return date1.getTime() > date2.getTime()
}

export default {
  defaultLang,
  getDayFull,
  getDayInitial,
  getDayAbbreviated,
  getMonthFull,
  getMonthAbbreviated,
  getDayOfMonth,
  humanize,
  clone,
  moveToDayOfWeek,
  isSameDay,
  isBefore,
  isAfter
}
