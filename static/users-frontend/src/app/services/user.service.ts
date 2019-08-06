import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {map} from "rxjs/operators";
import {User} from "../models/user";

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) {

  }

  getList(page:number) {
    return this.http.get(`/api/v1/users?page=${page}`).pipe(map(data => {
      let result = [];
      for (let index in data) {
        result.push(new User(data[index]))
      }
      return result;
    }))
  }

  get(id: number) {
    return this.http.get(`/api/v1/users/${id}`).pipe(map(data => new User(data)))
  }

  update(user: User) {
    return this.http.put(`/api/v1/users/${user.id}`, user).pipe(map(data => new User(data)))
  }

  delete(id) {
    return this.http.delete(`/api/v1/users/${id}`).pipe(map(data => data))
  }
}
