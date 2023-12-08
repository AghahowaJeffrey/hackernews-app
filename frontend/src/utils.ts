export function timeAgo(utcTime: string) {
  const timestampInSeconds = Date.parse(utcTime) / 1000;
  const currentTimeInSeconds = Date.now() / 1000;
  const timeDifference = Math.abs(currentTimeInSeconds - timestampInSeconds);

  const minutes = Math.floor(timeDifference / 60);
  const hours = Math.floor(timeDifference / 3600);
  const days = Math.floor(timeDifference / 86400);

  if (minutes < 60) {
    return `${pluralize(minutes, 'minute')} ago`;
  } else if (hours < 24) {
    return `${pluralize(hours, 'hour')} ago`;
  } else {
    return `${pluralize(days, 'day')} ago`;
  }
}

function pluralize(time: number, label: string) {
  return time === 1 ? `${time} ${label}` : `${time} ${label}s`;
}