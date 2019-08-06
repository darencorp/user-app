import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {UserInfoComponent} from './user-info/user-info.component';
import {UserListComponent} from './user-list/user-list.component';

const routes: Routes = [
  {path: '', component: UserListComponent},
  {path: 'user/:id', component: UserInfoComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {useHash: true})],
  exports: [RouterModule]
})
export class AppRoutingModule { }
