import {element} from './client.js';

function zone(target, className, text) {
  const box = element('div', undefined, {class:className});
  if (text) box.append(element('span',text));
  target.append(box);
  return box;
}

function fill(layer, value, max, label) {
  const mark = zone(layer, 'mark-piece', label);
  mark.style.setProperty('--part', `${Math.max(0,Math.min(100,100*value/Math.max(1,max)))}%`);
  return mark;
}

export function visualize(report, selected) {
  const target = document.querySelector('#visual');
  const row = report.cases?.find(item=>item.case===selected && item.measure);
  target.replaceChildren();
  if (!row) { target.append(element('p','该分组暂无计算值')); return; }
  const {evidence:e, value, expected, unit} = row.measure;
  render(target, e, value, expected, unit);
}

function render(target,e,value,expected,unit) {
  const points=zone(target,'peak-points');
  for(const [start,kw] of Object.entries(e.windows)) {
    const peak=Number(start)===e.peak_start_min;
    const point=zone(points,`peak-point ${peak?'peak-winner':''}`,`${start} min`);
    fill(point,kw,value,`${kw} kW`);
  }
}
