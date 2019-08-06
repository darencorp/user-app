import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { UserInfoComponent } from './user-info/user-info.component';
import { UserListComponent } from './user-list/user-list.component';

@NgModule({
  declarations: [
    UserListComponent,
    UserInfoComponent
  ],
  imports: [
    CommonModule,
    RouterModule
  ]
})
export class UsersModule { }
