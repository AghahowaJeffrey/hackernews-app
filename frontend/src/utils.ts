export function timeAgo (time: number | Date) {
    const between = Date.now() / 1000 - Number(time)
    if (between < 3600) { return pluralize(~~(between / 60), ' minute') } else if (between < 86400) { return pluralize(~~(between / 3600), ' hour') } else { return pluralize(~~(between / 86400), ' day') }
  }

  export function pluralize (time: number, label:string) {
    if (time === 1) { return time + label }
  
    return `${time + label}s`
  }
  