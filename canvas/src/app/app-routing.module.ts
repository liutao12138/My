import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';


const routes: Routes = [{
  path: 'demo1',
  loadChildren: () => import('app/demo/demo1/demo1.module').then(e => e.Demo1Module)
}, {
  path: '',
  redirectTo: 'demo1',
  pathMatch: 'full'
}];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
