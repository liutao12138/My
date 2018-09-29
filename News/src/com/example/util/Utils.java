package com.example.util;

import android.content.Context;

/**
 * 2018年9月29日 8:43:22 10437
 */
public class Utils
{
	private static final float HALF = 0.5f;
	
	/** px转dip */
	public static int px2dip(int px, Context context)
	{
		final float density = context.getResources().getDisplayMetrics().density;
		return (int) (px / density + HALF);
	}
	
	/** dip转px */
	public static int dip2px(int dp, Context context)
	{
		float density = context.getResources().getDisplayMetrics().density;
		return (int) (dp * density + HALF);
	}

	/** px转sp */
	public static int px2sp(int pxValue, Context context)
	{
		final float fontScale = context.getResources().getDisplayMetrics().scaledDensity;
		return (int) (pxValue / fontScale + HALF);
	}

	/** sp转px */
	public static int sp2px(int spValue, Context context)
	{
		final float fontScale = context.getResources().getDisplayMetrics().scaledDensity;
		return (int) (spValue * fontScale + HALF);
	}
}
