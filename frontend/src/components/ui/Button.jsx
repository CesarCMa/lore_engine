import clsx from 'clsx';
import LoadingSpinner from './LoadingSpinner';

export default function Button({
  children,
  variant = 'primary',
  size = 'md',
  isLoading = false,
  disabled = false,
  onClick,
  className,
  ...props
}) {
  const baseStyles = 'rounded-lg font-body font-semibold transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-arcane-500 focus:ring-offset-2';

  const variants = {
    primary: 'bg-gradient-to-r from-gold-500 to-gold-600 text-white hover:scale-105 hover:brightness-110 shadow-md hover:shadow-gold',
    secondary: 'bg-arcane-600 text-white hover:bg-arcane-700 shadow-md',
    danger: 'bg-crimson-600 text-white hover:bg-crimson-700 shadow-md',
    outline: 'border-2 border-gold-500 text-gold-600 hover:bg-gold-50 bg-transparent',
  };

  const sizes = {
    sm: 'px-3 py-1.5 text-sm',
    md: 'px-4 py-2 text-base',
    lg: 'px-6 py-3 text-lg',
  };

  const disabledStyles = 'opacity-50 cursor-not-allowed hover:scale-100 hover:brightness-100';

  return (
    <button
      onClick={onClick}
      disabled={disabled || isLoading}
      className={clsx(
        baseStyles,
        variants[variant],
        sizes[size],
        (disabled || isLoading) && disabledStyles,
        className
      )}
      {...props}
    >
      {isLoading ? (
        <span className="flex items-center justify-center gap-2">
          <LoadingSpinner size="sm" />
          <span>Loading...</span>
        </span>
      ) : (
        children
      )}
    </button>
  );
}
