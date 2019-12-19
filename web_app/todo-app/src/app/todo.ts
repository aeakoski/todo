export class Todo {
  id: number;
  title: string = '';
  desc: string = '';
  list_id:number;
  rank:number;
  complete: boolean;

  constructor(values: Object = {}) {
    Object.assign(this, values);
  }
}
