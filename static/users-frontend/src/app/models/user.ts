export class User {
  id: number;
  email: string;
  first_ame: string;
  last_name: string;
  avatar: string;

  constructor(input: any) {
    Object.assign(this, input);
  }
}
