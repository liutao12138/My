import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Demo1Component } from './demo1.component';
import { RouterModule } from '@angular/router';



@NgModule({
  declarations: [Demo1Component],
  imports: [
    CommonModule,
    RouterModule.forChild([{path: '', component: Demo1Component}])
  ]
})
export class Demo1Module { }
