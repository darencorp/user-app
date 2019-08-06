import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {UserListComponent} from './modules/users/user-list/user-list.component';
import {UserInfoComponent} from './modules/users/user-info/user-info.component';

const routes: Routes = [
  {path: '', component: UserListComponent},
  {path: 'user/:id', component: UserInfoComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {useHash: true})],
  exports: [RouterModule]
})
export class AppRoutingModule { }
