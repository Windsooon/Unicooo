//包含gulp   
var gulp = require('gulp');  

//包含我们的插件   

var less = require('gulp-less');
var minify = require('gulp-minify-css');
var jshint = require('gulp-jshint');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');

//lint task  

gulp.task('jshint',function(){
    gulp.src('statics/js/*.js')
    .pipe(jshint())
    .pipe(jshint.reporter('default'));
});

//编译less  

gulp.task('less',function(){
    gulp.src(['statics/unzip/less/*.less', '!statics/unzip/less/**/{reset,test}.less']) 
    .pipe(less())
    .pipe(minify())
    .pipe(gulp.dest('statics/zip/css'));
});  

//拼接、简化JS文件   

gulp.task('scripts',function(){
    gulp.src('statics/unzip/js/*.js')
    .pipe(concat('all.js'))
    .pipe(gulp.dest('statics/zip/minifyjs'))
    .pipe(rename('all.min.js'))
    .pipe(uglify())
    .pipe(gulp.dest('statics/zip/minifyjs'));
});  

//默认任务   
gulp.task('default',function(){
    gulp.run('jshint','less','scripts');

    //监视我们JS文件的变化   
    gulp.watch('statics/unzip/js/*.js',function(){
        gulp.run('lint','scripts');
    });

    //监视less文件的变化   
    gulp.watch('statics/unzip/less/*.less',function(){
        gulp.run('less');
    });
});   
