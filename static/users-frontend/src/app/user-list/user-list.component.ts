import {Component, OnInit} from '@angular/core';
import {UserService} from '../services/user.service';
import {User} from '../models/user';

@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.scss']
})
export class UserListComponent implements OnInit {

  userList: User[];
  page: number = 1;
  pages: number[] = [1, 2, 3];

  constructor(private users: UserService) {
  }

  ngOnInit() {
    this.users.getList(this.page).subscribe(data => {
      this.userList = data;
    });
  }

  changePage(page: number) {
    if (page > 2) {
      this.pages = [page-1, page, page+1]
    } else {
      if (this.pages[0] != 1) {
        this.pages = [1, 2, 3]
      }
    }

    this.page = page;

    this.users.getList(this.page).subscribe(data => {
      this.userList = data;
    })

  }
}
