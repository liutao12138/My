package com.example.news;

import com.example.news.adapter.CategoryAdapter;

import android.app.Activity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.ViewGroup.LayoutParams;
import android.widget.GridView;
import android.widget.LinearLayout;

public class MainActivity extends Activity
{
	
	@Override
	protected void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		String[] categories = this.getResources().getStringArray(R.array.categories);
		
		LayoutParams params = new LayoutParams(categories.length * 170 + categories.length, LayoutParams.WRAP_CONTENT);
		
		
		// 添加title
		GridView grid = new GridView(this);
		grid.setLayoutParams(params);
		grid.setNumColumns(categories.length);
		grid.setColumnWidth(160);
		grid.setAdapter(new CategoryAdapter(this, categories));
		LinearLayout scroll = (LinearLayout) this.findViewById(R.id.category_frame);
		scroll.addView(grid);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu)
	{
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

	@Override
	public boolean onOptionsItemSelected(MenuItem item)
	{
		// Handle action bar item clicks here. The action bar will
		// automatically handle clicks on the Home/Up button, so long
		// as you specify a parent activity in AndroidManifest.xml.
		int id = item.getItemId();
		if (id == R.id.action_settings)
		{
			return true;
		}
		return super.onOptionsItemSelected(item);
	}
}
