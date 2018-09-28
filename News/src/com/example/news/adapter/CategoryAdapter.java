package com.example.news.adapter;

import android.content.Context;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

/**
* 2018年9月28日 下午8:25:23 10437
*/
public class CategoryAdapter extends BaseAdapter
{
	
	private Context context;
	private String[] list;

	public CategoryAdapter(Context context, String[] list)
	{
		super();
		this.context = context;
		this.list = list;
	}

	@Override
	public int getCount()
	{
		return list.length;
	}

	@Override
	public Object getItem(int position)
	{
		return position;
	}

	@Override
	public long getItemId(int position)
	{
		return position;
	}

	@Override
	public View getView(int position, View convertView, ViewGroup parent)
	{
//		TextView text = null;
//		if  (null == convertView)
//		{
//			LayoutInflater.from(context).inflate(resource, root)
//		}
		TextView text = new TextView(context);
		text.setText(list[position]);
		return text;
	}

}

